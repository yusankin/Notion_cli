# tests/test_notion_cli.py

import os
from src.notion_cli import load_env

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