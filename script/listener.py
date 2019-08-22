from klein import Klein
import json


class listener:
    app = Klein()

    def __init__(self):
        print('start listener')
    
    @app.route('/', methods=['POST'])
    def handle_post(self, request):
        print('receive post')
        self.content = json.loads(str(request.content.read(), encoding='utf-8'))
        # print(content['r'])
        


if __name__ == '__main__':
    server = listener()
    server.app.run('localhost', 3001)


