import requests


class Ntfy:
    """
    ntfyのトピックにメッセージを送信するクラス
    """

    def __init__(self, server_url:str, topic_name:str, access_token:str):
        """
        Args:
            server_url   (str): ntfyサーバのURL
            topic_name   (str): トピック名
            access_token (str): アクセストークン
        """

        self.server_url   = server_url
        self.topic_name   = topic_name
        # サーバURLとトピック名を/区切りでつなげたものがエンドポイントになる
        self.endpoint_url = self.server_url + "/" + self.topic_name
        self.access_token = access_token


    def sendMessage(self, message:str, image_path:str=None) -> dict:
        """
        ntfyのトピックにメッセージを送信する

        Args:
            message (str): 送信するメッセージの本文
            image_path (str, optional): 送信する画像のファイルパス. Defaults to None.

        Returns:
            dict: ステータスコードとエラーメッセージが入った辞書
        """

        # アクセストークンの設定
        headers = {}
        if self.access_token is not None:
            headers = {'Authorization': f'Bearer {self.access_token}'}

        # ntfyのトピックにメッセージを送信
        response = requests.post(self.endpoint_url,
                                    data=message.encode(encoding='utf-8'),
                                    headers=headers)
        # TODO 画像送信を含めたメッセージの送信

        # 失敗した場合はエラーメッセージを取得
        if response.status_code != 200 and response.status_code != 204:
            message = f"code: {response.json()['code']}, http: {response.json()['http']}, error: {response.json()['error']}"
        else:
            message = 'Success'

        # ステータスコードとエラーメッセージを返す
        return {
            'status': response.status_code,
            'message': message,
        }
