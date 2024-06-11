import sys
import os

# スクリプトの絶対パスを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# モジュールのインポートパスを設定
sys.path.append(os.path.join(script_dir, 'src'))

from App import App

if __name__ == "__main__":
	root_app = App()
	root_app.mainloop()