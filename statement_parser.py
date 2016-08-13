#! /usr/bin/env python
import argparse
import statement_appfolio
import GlobalConstant as GC
import pm
# import address
# import activity
# import owner
import PyPDF2


class statement_parser(object):
    """This is where all the parsing and object creation happens"""

    def __init__(self, statement_file, vendor=appfolio):

        # ? Somehow in this method, we would magically figure out if it's appfolio or other statement type
        # A Let's suppose the user picks a vendor when calling the parser. For now, it's going to default to appfolio
        if vendor == 'appfolio':
            self.cur_statement = statement_appfolio()

        self.cur_statement.addStatementFile(statement_file)

    def parseStatement(self):
        # Populating a statement object(or its child class like statement_appfolio object)

        # 1. Raw pase in the statement file. Base on structure defined in GC, whenever a section is completed,
        # just pass that section to section_specific function as input.
        pdfFileObj = open(self.cur_statement.getStatementFile(), 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        raw_list = []

        # parsing in page at a time
        for page in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(page)
            raw_list = pageObj.extractText().split('\n')
            self.parseStatementList(raw_list)

        print self.cur_statement.getStatementFile()
        print "The following statement is imported"
        self.cur_statement.printStatement()

    def parseStatementList(self, raw_list):
        # Call each specific parsing function for each section, and pass in that list as input
        # section_parsing function should return

        section_raw_list = []
        for item in raw_list:
            # For each section found, we pass it to the statement class' corresponding method
            # Keep in mind, this is depend on the sequence of each section appearing in the raw list
            if item == GC.statement_structure_appfolio['pm_block_end_before']:
                # TBI -- statement_appfolio.addPm(), and pm.raw_import()
                # Need to handle if it's a different page, and things are repeated.
                # Maybe inside statement class' add function, it first checks if
                # the entry actually is the same, if so, don't add?
                self.cur_statement.addPm(section_raw_list)
                section_raw_list = []
                continue
            elif item == GC.statement_structure_appfolio['period_block_end_before']:
                self.cur_statement.addPeriod(section_raw_list)
                section_raw_list = []
                continue
            elif item == GC.statement_structure_appfolio['owner_block_end_before']:
                self.cur_statement.addOwner(section_raw_list)
                section_raw_list = []
                continue
            elif item == GC.statement_structure_appfolio['property_block_end_before']:
                self.cur_statement.addProperty(section_raw_list)
                section_raw_list = []
                continue
            elif item == GC.statement_structure_appfolio['table_block_end_before']:
                self.cur_statement.addActivity(section_raw_list)
                section_raw_list = []
                continue
            elif item == GC.statement_structure_appfolio['page_end_at']:
                # Anything to do if we reach end of a page?
                continue
            else:
                section_raw_list.append(item)





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Importing statement')
    parser.add_argument('-f', '--statement_file', help='Input file name', required=True)
    args = parser.parse_args()
    sparser = statement_parser(args.statement_file)
    statement = sparser.parseStatement()