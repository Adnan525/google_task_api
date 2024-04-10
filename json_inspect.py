# import json
#
#
# def main():
#     with open('task_test.json', 'r') as file:
#         data = json.load(file)
#
#     items = data['items']
#     for item in items:
#         title = item['title']
#         due_date = item['due']
#         print(f"Title: {title}, Due: {due_date}")
#
#
# if __name__ == "__main__":
#     main()
import json


def main():
    # Load the JSON file
    with open('task_test.json', 'r') as file:
        data = json.load(file)

    # Access all items and print title and due date
    items = data.get('items', [])  # Get list of items or empty list if 'items' key doesn't exist
    for item in items:
        title = item.get('title', 'Title not found')  # Get title or 'Title not found' if 'title' key doesn't exist
        due_date = item.get('due',
                            'Due date not found')  # Get due date or 'Due date not found' if 'due' key doesn't exist
        print(f"Title: {title}, Due: {due_date}")


if __name__ == "__main__":
    main()
