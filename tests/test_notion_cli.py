# tests/test_notion_cli.py
import os
import dotenv

import pytest
from src.env_loader import load_env
from src.notion_client import fetch_notion_data
from src.response_parser import (
    extract_titles_from_response,
    extract_select_from_response,
)
import requests


@pytest.fixture(scope="session")
def some_data():
    mock_response_data = {
        "object": "list",
        "results": [
            {
                "properties": {
                    "テキスト": {
                        "id": "IR%60%5B",
                        "type": "rich_text",
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": "sampletext2", "link": None},
                                "annotations": {
                                    "bold": False,
                                    "italic": False,
                                    "strikethrough": False,
                                    "underline": False,
                                    "code": False,
                                    "color": "default",
                                },
                                "plain_text": "sampletext2",
                                "href": None,
                            }
                        ],
                    },
                    "セレクト": {
                        "id": "eDPn",
                        "type": "select",
                        "select": {
                            "id": "5cf50c80-b4cf-409c-9a70-14882d39e215",
                            "name": "SAMPLE",
                            "color": "purple",
                        },
                    },
                    "Name": {
                        "id": "title",
                        "type": "title",
                        "title": [
                            {
                                "type": "text",
                                "text": {"content": "Sample Task 1", "link": None},
                                "annotations": {
                                    "bold": False,
                                    "italic": False,
                                    "strikethrough": False,
                                    "underline": False,
                                    "code": False,
                                    "color": "default",
                                },
                                "plain_text": "Sample Task 1",
                                "href": None,
                            }
                        ],
                    },
                },
            },
            {
                "properties": {
                    "テキスト": {
                        "id": "IR%60%5B",
                        "type": "rich_text",
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": "sampletext1", "link": None},
                                "annotations": {
                                    "bold": False,
                                    "italic": False,
                                    "strikethrough": False,
                                    "underline": False,
                                    "code": False,
                                    "color": "default",
                                },
                                "plain_text": "sampletext1",
                                "href": None,
                            }
                        ],
                    },
                    "セレクト": {
                        "id": "eDPn",
                        "type": "select",
                        "select": {"id": "E;|p", "name": "サンプル", "color": "blue"},
                    },
                    "Name": {
                        "id": "title",
                        "type": "title",
                        "title": [
                            {
                                "type": "text",
                                "text": {"content": "Sample Task 2", "link": None},
                                "annotations": {
                                    "bold": False,
                                    "italic": False,
                                    "strikethrough": False,
                                    "underline": False,
                                    "code": False,
                                    "color": "default",
                                },
                                "plain_text": "Sample Task 2",
                                "href": None,
                            }
                        ],
                    },
                },
            },
        ],
    }
    return mock_response_data


def test_load_env_reads_env_vars_correctly(monkeypatch):
    # テスト用に環境変数を上書き
    monkeypatch.setenv("NOTION_SECRET_ID", "sample_SECRET_ID")
    monkeypatch.setenv("NOTION_DB_ID", "sample_DB_ID")

    secret_id, db_id = load_env()

    assert secret_id == "sample_SECRET_ID"
    assert db_id == "sample_DB_ID"

    # テスト後に削除（他テストへの影響防止）
    monkeypatch.delenv("NOTION_SECRET_ID", raising=False)
    monkeypatch.delenv("NOTION_DB_ID", raising=False)


def test_fetch_notion_data_returns_expected_response(monkeypatch):
    # モックレスポンス定義（本来はAPIの返すJSON形式に合わせて）
    mock_response_data = {
        "results": [
            {
                "properties": {
                    "Name": {"title": [{"plain_text": "Sample Task 1"}]},
                    "Select": {"multiselect": [{"name": "Sample Select 1"}]},
                }
            },
            {
                "properties": {
                    "Name": {"title": [{"plain_text": "Sample Task 2"}]},
                    "Select": {"multiselect": [{"plain_text": "Sample Select 2"}]},
                }
            },
        ]
    }

    class MockResponse:
        def json(self):
            return mock_response_data

    def mock_post(*args, **kwargs):
        return MockResponse()

    # monkeypatchで requests.post を上書き
    monkeypatch.setattr(requests, "post", mock_post)

    # 実行して検証
    data = fetch_notion_data("dummy_secret", "dummy_db_id")
    assert data == mock_response_data


def test_extract_titles_from_response(some_data):
    expect = ["Sample Task 1", "Sample Task 2"]
    result = extract_titles_from_response(some_data)

    assert expect == result


def test_extract_select_from_response(some_data):
    except_selects = ["SAMPLE", "サンプル"]
    result = extract_select_from_response(some_data)
    assert result == except_selects
