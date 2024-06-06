import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from summarizer import TransformerSummarizer
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
def transcibe(link):
    model_id = "distil-whisper/distil-large-v3"

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True, attn_implementation="sdpa"
    )
    model.to(device)
    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=128,
        torch_dtype=torch_dtype,
        device=device,
    )
    sample = link
    result = pipe(sample, batch_size=8)
    GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2")
    Summary = ''.join(GPT2_model(result["text"], min_length=50))
    return Summary , len(result["text"]),len(Summary)

