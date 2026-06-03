import os
import requests

def get_original_file_name(response, file_id):
    if 'Content-Disposition' in response.headers:
        return response.headers['Content-Disposition'].split('filename=')[-1].strip('"')
    return file_id

def download_and_get_size(url, download_folder):
    print(f"\nDownloading from: {url}")

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_name = get_original_file_name(response, "other")
        
        if not os.path.exists(download_folder):
            os.makedirs(download_folder, exist_ok=True)

        save_path = os.path.join(download_folder, file_name)
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # 获取下载后的文件大小（单位：字节）
        file_size = os.path.getsize(save_path) 
        print(f"文件已保存至 {save_path}，大小为: {file_size / (1024*1024):.2f} MB")
    else:
        print(f"下载失败，状态码: {response.status_code}")


if __name__ == "__main__":
    download_folder = f"./dist"
    # Windows X-Lite “Ultimate 11” Cobalt v2                k7Fp3JuQ
    # Windows X-Lite “Ultimate 11 Neon” 24H2 v3             VUN49zuL
    # Windows X-Lite 'Ultimate 11' 24H2 Home                NU59tHU2
    # Windows X-Lite 'Optimum 11' 26H1 v2                   ZdPxkVmH


    download_and_get_size("https://pixeldrain.com/api/file/VUN49zuL?download", download_folder)