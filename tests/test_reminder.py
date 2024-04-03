from lib.reminder import *
import pytest

def test_reminder_is_init_with_a_name():
    reminder = Reminder('James')
    result = reminder.name
    assert result == 'James'

def test_remind_me_to_has_string_input():
    reminder = Reminder('James')
    reminder.remind_me_to('Walk the dog')
    result = reminder.remind()
    assert result == 'Your only task left is: Walk the dog'

def test_reminder_raises_exception_when_no_task():
    reminder = Reminder('James')
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == 'No task set.'

def test_remind_with_multiple_reminders():
    reminder = Reminder('James')
    reminder.remind_me_to('Walk the dog')
    reminder.remind_me_to('Clean the car')
    result = reminder.remind()
    assert result == 'James, your remaining tasks are:\n1) Walk the dog\n2) Clean the car\n'

def test_remind_with_multiple_reminders2():
    reminder = Reminder('James')
    reminder.remind_me_to('Walk the dog')
    reminder.remind_me_to('Clean the car')
    reminder.remind_me_to('Go to the gym')
    result = reminder.remind()
    assert result == 'James, your remaining tasks are:\n1) Walk the dog\n2) Clean the car\n3) Go to the gym\n'

def test_remind_complete_task():
    reminder = Reminder('James')
    reminder.remind_me_to('Walk the dog')
    reminder.remind_me_to('Clean the car')
    reminder.remind_me_to('Go to the gym')
    reminder.complete_task(3)
    result = reminder.remind()
    assert result == 'James, your remaining tasks are:\n1) Walk the dog\n2) Clean the car\n'

def test_complete_task_wrong_index():
    reminder = Reminder('James')
    reminder.remind_me_to('Walk the dog')
    reminder.remind_me_to('Clean the car')
    reminder.remind_me_to('Go to the gym')
    with pytest.raises(Exception) as e:
        reminder.complete_task(4)
    error_message = str(e.value)
    assert error_message == 'That is not a valid task number.'

def test_complete_task_no_tasks_to_complete():
    reminder = Reminder('James')
    with pytest.raises(Exception) as e:
        reminder.complete_task(1)
    error_message = str(e.value)
    assert error_message == 'No tasks to complete.'

