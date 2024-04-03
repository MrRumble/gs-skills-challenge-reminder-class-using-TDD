class Reminder():
    def __init__(self, name):
        self.name = name
        self.task_list = []
        self.is_reminder_set = False

    def remind_me_to(self, task):
        self.task_list.append(task)
        self.is_reminder_set = True

    def remind(self):
        if self.is_reminder_set == False:
            raise Exception('No task set.')
        if len(self.task_list) == 1:
            return f'Your only task left is: {self.task_list[0]}'
        task_string = f'{self.name}, your remaining tasks are:\n'
        for index, task in enumerate(self.task_list):
            task_string += f'{index + 1}) {task}\n'
        return task_string

    def complete_task(self, task_index):
        if len(self.task_list) == 0:
            raise Exception('No tasks to complete.')
        if task_index not in range(1, len(self.task_list)+1):
            raise Exception('That is not a valid task number.')
        else:
            self.task_list.pop(task_index - 1)
    
