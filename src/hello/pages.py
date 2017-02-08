
def get_globe():
    return globals()

class FirstPage(object):
    def get_heads(self):
        return [
            {'name':'slogan','label':'slogan','type':'blocktext',},
            {'name':'img','label':'brand','type':'linetext',}
        ]


class SecondPage(object):
    def get_heads(self):
        return [
            {'name':'name','label':'name','type':'linetext',}
        ]
    