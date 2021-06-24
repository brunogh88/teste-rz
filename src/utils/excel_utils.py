import win32com.client as win32
win32c = win32.constants

class ExelUtils(object):

    def __init__(self):
        self.excel = win32.gencache.EnsureDispatch('Excel.Application')
        self.excel.Visible = True  
        self.work_book = self.excel.Workbooks.Open(r"/data/excel/vendas-combustiveis-m3.xlsx")  
        self.pvtTable = self.work_book.Sheets("Plan1").Range("B53").PivotTable

    def __apply_filter(self, item_uf, item_product):
        self.pvtTable.PivotFields("UN. DA FEDERAÇÃO").CurrentPage = item_uf
        self.pvtTable.PivotFields("PRODUTO").CurrentPage = item_product

    def __load_data_excel(self):
        table_data = []
        for i in self.pvtTable.TableRange1:
            table_data.append(str(i))

        return self.table_data

    def __get_all_data_excel(self):

        table_data = self.__load_data_excel()

        list_search_values = ["Janeiro", "Fevereiro", "Março", 
                    "Abril", "Maio", "Junho", "Julho", 
                    "Agosto", "Setembro", "Outubro",
                    "Novembro", "Dezembro", "Total do Ano"]
        list_uf = ["ACRE", "ALAGOAS", "AMAPÁ", "AMAZONAS", "BAHIA", "CEARÁ", "DISTRITO FEDERAL",
                "ESPÍRITO SANTO", "GOIÁS", "MARANHÃO", "MATO GROSSO", "MATO GROSSO DO SUL",
                "MINAS GERAIS", "PARÁ", "PARAÍBA", "PARANÁ", "PERNAMBUCO", "PIAUÍ", "RIO DE JANEIRO",
                "RIO GRANDE DO NORTE", "RIO GRANDE DO SUL", "RONDÔNIA", "RORAIMA", "SANTA CATARINA",
                "SÃO PAULO", "SERGIPE", "TOCANTINS"]
        list_years = ["2000-01-01", "2001-01-01", "2002-01-01", "2003-01-01", "2004-01-01", "2005-01-01", 
                    "2006-01-01", "2007-01-01", "2008-01-01", "2009-01-01", "2010-01-01", 
                    "2011-01-01", "2012-01-01", "2013-01-01", "2014-01-01", "2015-01-01", "2016-01-01", 
                    "2017-01-01", "2018-01-01", "2019-01-01", "2020-01-01", "2021-01-01" ]
        list_products = ["ETANOL HIDRATADO (m3)", "GASOLINA C (m3)", "GASOLINA DE AVIÃO (m3)",
                        "GLP (m3)", "ÓLEO COMBUSTÍVEL (m3)", "ÓLEO DISEL (m3)", "QUEROSENE DE AVIAÇÃO (m3)",
                        "QUEROSENE ILUMINANTE (m3)"]

        df_all_data = None
        data_all_df = []

        for item_uf in list_uf: 
            for item_product in list_products: 
                table_data = self.__apply_filter(item_uf, item_product)
                print(table_data)
                for num_pos_search in range(len(list_search_values)-1):
                    idx_start = table_data.index(list_search_values[num_pos_search])
                    idx_finish = table_data.index(list_search_values[num_pos_search+1])
                    data = table_data[idx_start+1:idx_finish]
                    contador = 0
                    for value_sale in data:
                        if value_sale == 'None':
                            value_sale = '0'
                        data_all_df.append([list_years[contador], item_uf, item_product, "m3", value_sale])
                        contador = contador + 1

        return df_all_data   

    def genarete_csv(self):
        data_exel = self.__get_all_data_excel()
        df_all_data = self.spark.createDataFrame(data_exel,
            ["year_month", "uf", "product", "unit", "volume"])

        df_all_data.coalesce(1) \
        .write.option("header",True) \
        .option("delimiter",";") \
        .csv("/data/RAW/SALES_OIL_DERIVATIVE_FUELS/20210612")