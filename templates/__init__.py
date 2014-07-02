from web.template import CompiledTemplate, ForLoop, TemplateResult

import hidden
# coding: utf-8
def formtest (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<html>\n'])
    extend_([u'    <link rel="stylesheet" href="/static/style.css" type="text/css"/>\n'])
    extend_([u'    <form name="main" method="post"> \n'])
    if not form.valid:
        extend_(['    ', u'<p class="error">Try again, AmeriCAN:</p>\n'])
    extend_([u'    ', escape_(form.render(), False), u'\n'])
    extend_([u'<input type="submit" />    </form>\n'])
    extend_([u'</html>\n'])
    extend_([u'\n'])

    return self

formtest = CompiledTemplate(formtest, 'templates\\formtest.html')
join_ = formtest._join; escape_ = formtest._escape

# coding: utf-8
def index (old_life, new_life, country1, country2, change):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<html>\n'])
    extend_([u'<font face="Helvetica", font size = 4>\n'])
    extend_([u'<p> Right now, if you stay in ', escape_(country1, True), u' you have about ', escape_(round(old_life,2), True), u' years left.</p>\n'])
    extend_([u'<p> If you move to ', escape_(country2.capitalize(), True), u', you can expect to live about ', escape_(round(new_life,2), True), u' years.</p>\n'])
    if change>0:
        extend_([u'    <p> That means that if you move to ', escape_(country2, True), u' now, your lifespan will increase by ', escape_(round(change,2), True), u' years!</p>\n'])
    else:
        extend_([u'    <p> Dude, are you sure? If you move to ', escape_(country2, True), u", your remaining life expectancy will drop! It'll change by ", escape_(round(change,2), True), u' years.</p>\n'])
    extend_([u'</font>\n'])
    extend_([u'</html>\n'])

    return self

index = CompiledTemplate(index, 'templates\\index.html')
join_ = index._join; escape_ = index._escape

