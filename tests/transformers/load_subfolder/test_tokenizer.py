# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import unittest

from paddlenlp.transformers import (
    AutoTokenizer,
    BertTokenizer,
    CLIPTokenizer,
    T5Tokenizer,
)
from paddlenlp.utils.log import logger
from tests.testing_utils import slow


class TokenizerLoadTester(unittest.TestCase):
    @slow
    def test_bert_load(self):
        logger.info("Download model from PaddleNLP BOS")
        bert_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased", from_hf_hub=False)
        bert_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased", from_hf_hub=False)

        logger.info("Download model from local")
        bert_tokenizer.save_pretrained("./paddlenlp-test-model/bert-base-uncased")
        bert_tokenizer = BertTokenizer.from_pretrained("./paddlenlp-test-model/bert-base-uncased")
        bert_tokenizer = AutoTokenizer.from_pretrained("./paddlenlp-test-model/bert-base-uncased")
        bert_tokenizer = BertTokenizer.from_pretrained("./paddlenlp-test-model/", subfolder="bert-base-uncased")
        bert_tokenizer = AutoTokenizer.from_pretrained("./paddlenlp-test-model/", subfolder="bert-base-uncased")

        logger.info("Download model from PaddleNLP BOS with subfolder")
        bert_tokenizer = BertTokenizer.from_pretrained(
            "baicai/paddlenlp-test-model", subfolder="bert-base-uncased", from_hf_hub=False
        )
        bert_tokenizer = AutoTokenizer.from_pretrained(
            "baicai/paddlenlp-test-model", subfolder="bert-base-uncased", from_hf_hub=False
        )

        logger.info("Download model from aistudio")
        bert_tokenizer = BertTokenizer.from_pretrained("aistudio/bert-base-uncased", from_aistudio=True)
        bert_tokenizer = AutoTokenizer.from_pretrained("aistudio/bert-base-uncased", from_aistudio=True)

        logger.info("Download model from aistudio with subfolder")
        bert_tokenizer = BertTokenizer.from_pretrained(
            "aistudio/paddlenlp-test-model", subfolder="bert-base-uncased", from_aistudio=True
        )
        bert_tokenizer = AutoTokenizer.from_pretrained(
            "aistudio/paddlenlp-test-model", subfolder="bert-base-uncased", from_aistudio=True
        )

    @slow
    def test_clip_load(self):
        logger.info("Download model from PaddleNLP BOS")
        clip_tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-base-patch32", from_hf_hub=False)
        clip_tokenizer = AutoTokenizer.from_pretrained("openai/clip-vit-base-patch32", from_hf_hub=False)

        logger.info("Download model from local")
        clip_tokenizer.save_pretrained("./paddlenlp-test-model/clip-vit-base-patch32")
        clip_tokenizer = CLIPTokenizer.from_pretrained("./paddlenlp-test-model/clip-vit-base-patch32")
        clip_tokenizer = AutoTokenizer.from_pretrained("./paddlenlp-test-model/clip-vit-base-patch32")
        clip_tokenizer = CLIPTokenizer.from_pretrained("./paddlenlp-test-model/", subfolder="clip-vit-base-patch32")
        clip_tokenizer = AutoTokenizer.from_pretrained("./paddlenlp-test-model/", subfolder="clip-vit-base-patch32")

        logger.info("Download model from PaddleNLP BOS with subfolder")
        clip_tokenizer = CLIPTokenizer.from_pretrained(
            "baicai/paddlenlp-test-model", subfolder="clip-vit-base-patch32", from_hf_hub=False
        )
        clip_tokenizer = AutoTokenizer.from_pretrained(
            "baicai/paddlenlp-test-model", subfolder="clip-vit-base-patch32", from_hf_hub=False
        )

        logger.info("Download model from aistudio")
        clip_tokenizer = CLIPTokenizer.from_pretrained("aistudio/clip-vit-base-patch32", from_aistudio=True)
        clip_tokenizer = AutoTokenizer.from_pretrained("aistudio/clip-vit-base-patch32", from_aistudio=True)

        logger.info("Download model from aistudio with subfolder")
        clip_tokenizer = CLIPTokenizer.from_pretrained(
            "aistudio/paddlenlp-test-model", subfolder="clip-vit-base-patch32", from_aistudio=True
        )
        clip_tokenizer = AutoTokenizer.from_pretrained(
            "aistudio/paddlenlp-test-model", subfolder="clip-vit-base-patch32", from_aistudio=True
        )

    @slow
    def test_t5_load(self):
        logger.info("Download model from PaddleNLP BOS")
        t5_tokenizer = T5Tokenizer.from_pretrained("t5-small", from_hf_hub=False)
        t5_tokenizer = AutoTokenizer.from_pretrained("t5-small", from_hf_hub=False)

        logger.info("Download model from local")
        t5_tokenizer.save_pretrained("./paddlenlp-test-model/t5-small")
        t5_tokenizer = T5Tokenizer.from_pretrained("./paddlenlp-test-model/t5-small")
        t5_tokenizer = AutoTokenizer.from_pretrained("./paddlenlp-test-model/t5-small")
        t5_tokenizer = T5Tokenizer.from_pretrained("./paddlenlp-test-model/", subfolder="t5-small")
        t5_tokenizer = AutoTokenizer.from_pretrained("./paddlenlp-test-model/", subfolder="t5-small")

        logger.info("Download model from PaddleNLP BOS with subfolder")
        t5_tokenizer = T5Tokenizer.from_pretrained(
            "baicai/paddlenlp-test-model", subfolder="t5-small", from_hf_hub=False
        )
        t5_tokenizer = AutoTokenizer.from_pretrained(
            "baicai/paddlenlp-test-model", subfolder="t5-small", from_hf_hub=False
        )

        logger.info("Download model from aistudio")
        t5_tokenizer = T5Tokenizer.from_pretrained("aistudio/t5-small", from_aistudio=True)
        t5_tokenizer = AutoTokenizer.from_pretrained("aistudio/t5-small", from_aistudio=True)

        t5_tokenizer = T5Tokenizer.from_pretrained(
            "aistudio/paddlenlp-test-model", subfolder="t5-small", from_aistudio=True
        )
        t5_tokenizer = AutoTokenizer.from_pretrained(
            "aistudio/paddlenlp-test-model", subfolder="t5-small", from_aistudio=True
        )
