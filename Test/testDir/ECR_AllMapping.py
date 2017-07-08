from openpyxl import load_workbook
import csv, logging

SOURCE_FILE = 'C:/Users/Dharmendra.Mishra/Box Sync/ExpoTeamSpaces/Departments/Operations/Business Intelligence/Reports/Business Intelligence ECR/Automation/All Files/ECR_All_Mapping.xlsx'
OUTPUT_SHEETS = {'tfcrIoDetails': 'C:/BiUiGit/data/mapping/tfcr/tfcrIoDetails.csv',
                 'tfcrLabelIoIds': 'C:/BiUiGit/data/reportSpecs/tfcrLabelIoIds.csv',
                 'ThirdPartySubjectLine': 'C:/BiUiGit/data/mapping/tfcr/ThirdPartySubjectLine.csv',
                 'dartIoPlacementItemName': 'C:/BiUiGit/data/mapping/tfcr/dartIoPlacementItemName.csv',
                 'dartDatePlacementConversion': 'C:/BiUiGit/data/mapping/tfcr/dartDatePlacementConversionColumn.csv',
                 'dartDatePlacementRevenue': 'C:/BiUiGit/data/mapping/tfcr/dartDatePlacementRevenueColumn.csv',
                 'dartF2IoPlacementItemName': 'C:/BiUiGit/data/mapping/tfcr/dartF2IoPlacementItemName.csv',
                 'dartF2DatePlacementConversion': 'C:/BiUiGit/data/mapping/tfcr/dartF2DatePlacementConversionColumn.csv',
                 'dartF2DatePlacementRevenue': 'C:/BiUiGit/data/mapping/tfcr/dartF2DatePlacementRevenueColumn.csv',
                 'dartMCCIoPlacementItemName': 'C:/BiUiGit/data/mapping/tfcr/dartMCCIoPlacementItemName.csv',
                 'dartMCCDatePlacementConversion': 'C:/BiUiGit/data/mapping/tfcr/dartMCCDatePlacementConversionColumn.csv',
                 'dartF2MCCIoPlacementItemName': 'C:/BiUiGit/data/mapping/tfcr/dartF2MCCIoPlacementItemName.csv',
                 'dartF2MCCDatePlacementConver': 'C:/BiUiGit/data/mapping/tfcr/dartF2MCCDatePlacementConversionColumn.csv',
                 'atlasIoPlacementItemName': 'C:/BiUiGit/data/mapping/tfcr/atlasIoPlacementItemName.csv',
                 'atlasDatePlacementConversion': 'C:/BiUiGit/data/mapping/tfcr/atlasDatePlacementConversionColumn.csv',
                 'atlasDatePlacementRevenue': 'C:/BiUiGit/data/mapping/tfcr/atlasDatePlacementRevenueColumn.csv',
                 'atlasF2IoPlacementItemName': 'C:/BiUiGit/data/mapping/tfcr/atlasF2IoPlacementItemName.csv',
                 'atlasF2DatePlacementConversion': 'C:/BiUiGit/data/mapping/tfcr/atlasF2DatePlacementConversionColumn.csv',
                 'atlasMCCIoPlacementItemName': 'C:/BiUiGit/data/mapping/tfcr/atlasMCCIoPlacementItemName.csv',
                 'atlasMCCDatePlacementConversion': 'C:/BiUiGit/data/mapping/tfcr/atlasMCCDatePlacementConversionColumn.csv',
                 'atlasF2MCCIoPlacementItemName': 'C:/BiUiGit/data/mapping/tfcr/atlasF2MCCIoPlacementItemName.csv',
                 'atlasF2MCCDatePlacementConvers': 'C:/BiUiGit/data/mapping/tfcr/atlasF2MCCDatePlacementConversionColumn.csv',
                 'mediaMindIoPlacementItemName': 'C:/BiUiGit/data/mapping/tfcr/mediaMindIoPlacementItemName.csv',
                 'mediaMindDatePlacementConvers': 'C:/BiUiGit/data/mapping/tfcr/mediaMindDatePlacementConversionColumn.csv',
                 'mediaMindF2IoPlacementItemName': 'C:/BiUiGit/data/mapping/tfcr/mediaMindF2IoPlacementItemName.csv',
                 'mediaMindF2DatePlacementConvers': 'C:/BiUiGit/data/mapping/tfcr/mediaMindF2DatePlacementConversionColumn.csv',
                 'mediaMindF2DatePlacementRevenue': 'C:/BiUiGit/data/mapping/tfcr/mediaMindF2DatePlacementRevenueColumn.csv',
                 'mediamindMCCIoPlacementItemName': 'C:/BiUiGit/data/mapping/tfcr/mediamindMCCIoPlacementItemName.csv',
                 'mediamindMCCDatePlacementConv': 'C:/BiUiGit/data/mapping/tfcr/mediamindMCCDatePlacementConversionColumn.csv',
                 'mediaMindF2MCCIoPlacementItem': 'C:/BiUiGit/data/mapping/tfcr/mediaMindF2MCCIoPlacementItemName.csv',
                 'mediaMindF2MCCDatePlacementConv': 'C:/BiUiGit/data/mapping/tfcr/mediaMindF2MCCDatePlacementConversionColumn.csv'}

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s')


def push_row(rows_tobe_pushed, sheet_name):
    with open(OUTPUT_SHEETS.get(sheet_name), 'a', newline="\n") as f:
        writer = csv.writer(f)
        for row in rows_tobe_pushed:
            cells = [cell.value for cell in row]
            writer.writerow(cells[:-1])
            logging.debug('%s has written to %s.csv', cells, sheet_name)


def process_source_file(source_file):
    wb = load_workbook(source_file)
    logging.info('Loaded %s', source_file)
    for sheet_name in OUTPUT_SHEETS.keys():
        sheet = wb.get_sheet_by_name(sheet_name)
        logging.info('Loaded sheet: %s', sheet_name)
        rows = [row for row in sheet.rows]
        rows_tobe_pushed = []
        for idx, row in enumerate(rows[0:], start=17):
            cells = [cell.value for cell in row]
            if str(cells[-1]) in ('no', 'No', 'NO'):
                rows_tobe_pushed.append(row)
                sheet['%s%s' % (chr(64 + len(cells)), idx)] = 'Yes'
                logging.debug('%s has appended for pushing', cells)
        push_row(rows_tobe_pushed, sheet_name)
    wb.save(source_file)


def main():
    logging.info('Started to process %s', SOURCE_FILE)
    process_source_file(SOURCE_FILE)


if __name__ == '__main__':
    main()




