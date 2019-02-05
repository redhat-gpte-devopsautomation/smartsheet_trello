#!/usr/bin/env python3
import os, sys
import argparse
import smartsheet
from trello import TrelloClient


def get_tasks(sheet_id):
    ss = smartsheet.Smartsheet(smartsheet_token)
    ss.errors_as_exceptions(True)
    try:
        raw_sheet = ss.Sheets.get_sheet(sheet_id)
    except:
        print("Something is wrong...")
        sys.exit(1)

    sheet = raw_sheet.to_dict()
    title_column_id = [c['id'] for c in sheet['columns'] if c['title'] == 'Task Name'][0]
    row_tasks =[]
    for r in sheet['rows']:
        task = [c['displayValue'] for c in r['cells'] if c['columnId'] ==
                title_column_id][0]
        if 'parentId' in r.keys():
            par_id = r['parentId']
        else:
            par_id = None
        row_tasks.append([par_id, r['id'], task])

    return row_tasks


def card_names(row_tasks):
    # head of the list is the row with DEVELOPMENT in Task Name
    dev_id = [t[1] for t in row_tasks if t[2] == 'DEVELOPMENT'][0]

    modules = [t for t in row_tasks if t[0] == dev_id]

    names = []
    for m in modules:
        module_tasks = [t for t in row_tasks if t[0] == m[1]]
        for task in module_tasks:
            name = m[2] + ": " + task[2]
            names.append(name)

    return names


def add_list_to_board(board_id, list_name):
    client = TrelloClient(api_key=trello_api_key, api_secret=trello_api_token)
    board = client.get_board(board_id=board_id)
    l = board.add_list(name=list_name)
    
    return l.id
    

def main():
    if 'TRELLO_API_KEY' not in os.environ:
        print("TRELLO_API_KEY environment variable is not set. Exiting...")
        sys.exit(1)
    if 'TRELLO_API_TOKEN' not in os.environ:
        print("TRELLO_API_TOKEN environment variable is not set. Exiting...")
        sys.exit(1)
    if 'SMARTSHEET_TOKEN' not in os.environ:
        print("SMARTSHEET_TOKEN environment variable is not set. Exiting...")
        sys.exit(1)

    global trello_api_key
    global trello_api_token
    global smartsheet_token
    trello_api_key = os.environ['TRELLO_API_KEY']
    trello_api_token = os.environ['TRELLO_API_TOKEN']
    smartsheet_token = os.environ['SMARTSHEET_TOKEN']

    # borrowed from here: https://stackoverflow.com/questions/24180527/argparse-required-arguments-listed-under-optional-arguments
    parser = argparse.ArgumentParser()
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    required.add_argument('-s', '--smartsheet', help='Smartsheet ID',
                          required=True)
    required.add_argument('-t', '--trello', help='Trello Board name',
                          required=True)
    args = parser.parse_args()

    smartsheet_id = args.smartsheet
    trello_board = args.trello

    rt = get_tasks(smartsheet_id)
    list_name = [t[2] for t in rt if t[0] == None][0]

    print("List name: ",  list_name)
    cards = card_names(rt)

    try:
        client = TrelloClient(api_key=trello_api_key, api_secret=trello_api_token)
    except Exception as e:
        print("Trello problem: ", e)
        sys.exit(1)

    try:
        t_board = [b for b in client.list_boards() if b.name == trello_board][0]
    except IndexError:
        print("Board not found: ", trello_board)
        sys.exit(1)

    list_id = add_list_to_board(t_board.id, list_name)
    test_list = t_board.get_list(list_id=list_id)

    for c in cards:
        test_list.add_card(name=c)
        print('Added card: ', '"', c, '"')

    print('Done')



if __name__ == '__main__':
    main()
