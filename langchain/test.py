from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain

data = [{'context': 'FÍSICA - QUÍMICA',
  'question_id': '-97996',
  'question_name': 'La sustancia química que tiene propiedades definidas y que, conserva su composición química dentro de una mezcla, se denomina:',
  'answers': [{'answer_id': '-378714', 'answer_name': 'elemento.'},
   {'answer_id': '-378715', 'answer_name': 'solución.'},
   {'answer_id': '-378716', 'answer_name': 'componente.'}]}]

prompt_template_es = """Eres un experto en {context}.
Tu tarea es validar las opciones de respuesta a esta pregunta:
{question_name}

Estas son las únicas opciones de respuesta:
{answers}

Por cada opción, indica si es correcta o incorrecta.
"""

prompt = PromptTemplate(template=prompt_template_es, input_variables=["context", "question_name", "answers"])

local_path = (
    "./models/wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin" 
)

callbacks = [StreamingStdOutCallbackHandler()]

llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True, temp=0.0, n_predict=1000)

llm_chain = LLMChain(prompt=prompt, llm=llm)

predictions = llm_chain.apply(data)

print(predictions)