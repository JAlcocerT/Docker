#pip install gradio_client


from gradio_client import Client

from gradio_client import Client

client = Client("http://localhost:8001/")
result = client.predict(
		"What is flutter?",	# str  in 'Message' Textbox component
		api_name="/chat"
)
print(result)


# client = Client("http://localhost:8001/")
# result = client.predict(
# 		"https://github.com/gradio-app/gradio/raw/main/test/test_files/sample_file.pdf",	# str (filepath on your computer (or URL) of file) in 'Upload a File' Uploadbutton component
# 		fn_index=0
# )
# print(result)