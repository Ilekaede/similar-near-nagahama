from icrawler.builtin import BingImageCrawler # bingで集める
import sys
import os

argv = sys.argv

if len(argv) != 3: # コマンドライン引数が規定の個数を満たしていないとき
    print("Usage: python image_crawler.py <directory> <keyword>")
    sys.exit(1)

output_dir = argv[1]
keyword = argv[2]

if not os.path.isdir(output_dir): # 保存先のフォルダが存在しない場合には作成する
    os.makedirs(output_dir)

bing_crawler = BingImageCrawler(storage={"root_dir": output_dir})

print(f"Crawling images for keyword: {keyword} into directory: {output_dir}")
bing_crawler.crawl(keyword=keyword, max_num=1000)
print("Crawling finished.")
