from xlsxwriter import Workbook

def dict2xlsx(dictlist, xlsxfile):
    """
    Takes a list of dictionaries as input and outputs a XLSX file.
    """
    wb = Workbook(xlsxfile)
    ws = wb.add_worksheet("Plan-105")  # Or leave it blank. The default name is "Sheet 1"

    first_row = 0
    headers = list(dictlist[0].keys())
    for header in headers:
        col = headers.index(header)  # We are keeping order.
        ws.write(first_row, col,
                 header)  # We have written first row which is the header of worksheet also.

    row = 1
    for player in dictlist:
        if player['AMOUNT'] not in (0, "0", 0.0, "0.0"):
            for _key, _value in player.items():
                col = headers.index(_key)
                ws.write(row, col, _value)
            row += 1  # enter the next row

    wb.close()