import requests

from tqdm import tqdm

response = requests.get(url, stream=True)  # 把stream参数设置为True
file_size = int(response.headers['Content-Length'])
chunk = 1
chunk_size = 1024
num_bars = int(file_size / chunk_size)
with open(filename, 'wb') as fp:
    for chunk in tqdm(response.iter_content(chunk_size=chunk_size), total=num_bars, unit='KB', desc=filename,
                      leave=True):
        fp.write(chunk)
