import csv
import subprocess

def generate_dns_requests(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            domain = row[0]
            subprocess.run(['dig', domain])

if __name__ == '__main__':
    generate_dns_requests('/app/3rd_lev_domains.csv')
