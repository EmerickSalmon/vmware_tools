
def wait_for_task(object_name:str, task):
    task_info = None
    try:
        task.wait()
        task_info = task.info
    except Exception as e:
        # TODO: Create custom error
        message = f"Error while perfom task for object '{object_name}': {e}"
        print(message)
        raise Exception(message)
        

    if task_info.state == "error":
        # TODO: Create custom error
        message = f"Error while perfom task for object '{object_name}': {e}"
        print(message)
        raise Exception(message)        

    print(f"Tasks done for object {object_name}")

    
