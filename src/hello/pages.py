
def get_globe():
    return globals()

class FirstPage(object):
    template='hello/first_page.html'
    def get_heads(self):
        return [
            {'name':'slogan','label':'slogan','type':'richtext',},
            {'name':'content','label':'content','type':'richtext',},
            {'name':'foot','label':'foot','type':'richtext',}
        ]


class SecondPage(object):
    def get_heads(self):
        return [
            {'name':'name','label':'name','type':'linetext',}
        ]
    