import csv
from django.core.management.base import BaseCommand
from InventorySystem.models import Hardware



class Command(BaseCommand):
    help = 'Import inventory data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):

        # Get the path to the CSV file from the command-line argument
        csv_file = kwargs['csv_file']


        # Open the CSV and read its contents
        with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

                     #debug lines
                        # Print the fieldnames
            print("Fieldnames:", reader.fieldnames)

            # Iterate over each row in the CSV file
            for row in reader:

                # Print row to inspect its contents
                print("Row:", row)

                    #//




            
            # Iterate over each row in inventory file
            for row in reader:

                # Create a new Equipment object for each row 
                Hardware_item = Hardware(
                    DeviceName=row['Device Name'],
                    quantity=row['Quantity'],
                    Type =row['Device Type'],
                    Audit =row['Audit'],
                    Location =row['Location'],
                    Status =row['Status'],
                    Comments =row['Comments'],
                    DeviceSerial =row['Device Serial'],
                    CPU =row['CPU'],
                    GPU =row['GPU'],
                    RAM =row['RAM'],
                )


                
                # Save hardware to the database
                Hardware_item.save()



        # successful import
        self.stdout.write(self.style.SUCCESS('Inventory data imported successfully'))
