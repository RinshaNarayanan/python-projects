import pytest
from todo import TodoList 

def test_add_item():
    todo_list = TodoList()
    todo_list.add_item("Study for exam")

    assert todo_list.view_item() == ["Study for exam"]

def test_remove_item():
    todo_list = TodoList()
    todo_list.add_item("complete assignment")
    todo_list.add_item("submit project report")
    final = todo_list.remove_item(1)
    assert todo_list.view_item() == ["complete assignment"]

def test_listing_item():
    todo_list = TodoList()
    todo_list.add_item("complete assignment")
    todo_list.add_item("submit project report")
    assert todo_list.view_item() == ["complete assignment", "submit project report",]

test_listing_item()

