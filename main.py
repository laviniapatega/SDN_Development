import requests
import time
from data_structures.datacenter import Datacenter

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data(dict)
    """
    retries = 1

    while retries <= max_retries:
        try:

            response = requests.get(url)
            data = response.json()
            return data

        except Exception:
            print("Request failed, keep retrying...")
            time.sleep(delay_between_retries)
            retries += 1


def main():
    """
    Main entry to our program.
    """
    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')
    else:
        print(data)

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    # Remove invalid clusters
    for datacenter in datacenters:
        datacenter.remove_invalid_clusters()

    # Remove invalid records and sort them
    for datacenter in datacenters:
        for cluster in datacenter.clusters:
            for network in cluster.networks:
                network.remove_invalid_records()
                network.sort_records()

    print(datacenters)
    # Write the output as a string in output.txt (only for testing)
    f = open('output.txt', 'w')
    f.write(str(datacenters))


if __name__ == '__main__':
    main()
