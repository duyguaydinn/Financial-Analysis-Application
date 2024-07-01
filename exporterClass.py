import pandas as pd

class Exporter:
    def __init__(self, data):
        self.data = data

    def export_to_csv(self, file_path):
        try:
            self.data.to_csv(file_path, index=False)
        except Exception as e:
            print(f"An error occurred while exporting to CSV: {e}")

    def export_to_xlsx(self, file_path):
        try:
            self.data.to_excel(file_path, index=False)
        except Exception as e:
            print(f"An error occurred while exporting to XLSX: {e}")

