class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = "<{}>".format(name)
        self.end_tag = "</{}>".format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''  # DocType doesn't have any end tag


class Head(Tag):

    def __init__(self, title=None):
        super().__init__('Head', '')
        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__('Body', '')
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)
            # 这里又学会了，可以直接将对象转换为设定的str类型输出，即直接调用对象的__str__函数。

        super().display(file=file)


class HtmlDoc(object):

    # def __init__(self, title=None):
    #     self._doc_type = DocType()
    #     self._head = Head(title)
    #     self._body = Body()

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file):
        self._doc_type.display(file=file)
        print("<html>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == "__main__":
    # my_page = HtmlDoc("Demo HTML Document")
    # my_page.add_tag("h1", "Main heading")
    # my_page.add_tag('h2', "sub_heading")
    # my_page.add_tag('p', "This is a paragraph will appear on the page")
    # with open('test.html', 'w') as test_doc:
    #     my_page.display(file=test_doc)
    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances"
                          " of object to build up another object.")
    new_body.add_tag('p', "The composed object doesn't actually own the objects that it's composed of"
                          " - if it's destroyed, those objects continue to exist.")
    new_doc_type = DocType()
    new_header = Head("Aggregation document")
    my_page = HtmlDoc(new_doc_type, new_header, new_body)
    with open('test3.html', 'w') as test_doc:
        my_page.display(file=test_doc)

# new_body = Body()
# new_body.add_tag('h1', 'Aggregation')
# new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances"
#                       " of object to build up another object.")
# new_body.add_tag('p', "The composed object doesn't actually own the objects that it's composed of"
#                       " - if it's destroyed, those objects continue to exist.")

# give our document new content by switching its body
# my_page._body = new_body
# with open('test2.html', 'w') as test_doc:
#     my_page.display(file=test_doc)
    # print("*" * 80)
    # test_tag = Tag("test_tag", "")
    # print(str(test_tag))
    # print(test_tag)

