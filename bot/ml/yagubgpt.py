import torch
from transformers import AutoModelWithLMHead, AutoTokenizer


class YagubGPT:
    def __init__(self, model_path, state_dict_path=None):
        self.model = AutoModelWithLMHead.from_pretrained(model_path, ignore_mismatched_sizes=True)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, return_tensors='pt')
        self.model.resize_token_embeddings(len(self.tokenizer))

        if not state_dict_path is None:
            self.model.load_state_dict(torch.load(state_dict_path, map_location=torch.device('cpu')))
            self.model.eval()

    def answer(self, prompt):
        tokenized_text = self.tokenizer.encode(prompt, return_tensors='pt')
        answer = self.tokenizer.decode(self.model.generate(tokenized_text)[0])

        return answer, answer.split("<|endoftext|>")

