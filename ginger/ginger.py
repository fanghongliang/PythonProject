"""
Created by Fanghl on 2020/9/10 11:51
"""

from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)