from astic.service import get_prompt_image
from gpt.service import call_chatgpd


astic_key = 'XXX'
visionParams = 'gpt_detailed,describe'
chatgpd_key = 'XXX'
chatgpd_model = 'gpt-4'
image = 'https://i.ibb.co/VJJ9rr9/image-G2d-MH0-Kg-Uk-WTFqp9lv-Ot-Fg.jpg'

image_result = get_prompt_image(asticaAPI_key=astic_key, httpsImage=image, visionParams=visionParams)

####CONTEXT CHATGPD RESULT FINAL

chat_messages = []
chat_messages.append({"role": "assistant", "content": 'You are a robot that creates company reports based on informations.'})
chat_messages.append({"role": "user", "content": f'Generate a report based on the following information about the image registered: {image_result}'})

final_result = call_chatgpd(api_key=chatgpd_key, model=chatgpd_model, chat_messages=chat_messages)

print(final_result)


"""

A imagem retrata uma sacola plástica cheia de resíduos, com nível de confiança de aproximadamente 76,94%. 
O saco plástico, possivelmente feito de polietileno ou material semelhante, parece estar bastante cheio de vários itens de lixo, 
indicando que foi utilizado em sua capacidade máxima.

"""