import re

def intelligent_chunk(text, max_len=280):
    paragraphs = re.split(r'\n\s*\n', text.strip())  # Split on empty lines
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        para = para.strip().replace('\n', ' ')
        if len(para) <= max_len:
            if len(current_chunk) + len(para) + 1 <= max_len:
                current_chunk += " " + para if current_chunk else para
            else:
                chunks.append(current_chunk.strip())
                current_chunk = para
        else:
            # break longer paragraph into sentences
            sentences = re.split(r'(?<=[.?!])\s+', para)
            for sentence in sentences:
                if len(current_chunk) + len(sentence) + 1 <= max_len:
                    current_chunk += " " + sentence if current_chunk else sentence
                else:
                    chunks.append(current_chunk.strip())
                    current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk.strip())

    return [f"{chunk}\n{i+1}/{len(chunks)}" for i, chunk in enumerate(chunks)]
