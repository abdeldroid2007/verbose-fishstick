from hugchat import hugchat
from hugchat.login import Login

EMAIL = "984margo@finacenter.com"
PASSWD = "Simou@2007"
sign = Login(EMAIL, PASSWD)
cookies = sign.login(save_cookies=True)
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
def answer(query):
    query_result = chatbot.chat(query)
    return query_result
print(answer(prompt))
