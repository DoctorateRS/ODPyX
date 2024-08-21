from typing import Any
from msgspec.json import Encoder, Decoder, format


class Json:
    encoder: Encoder
    decoder: Decoder

    def __init__(self):
        self.encoder = Encoder(decimal_format="number", order="deterministic")
        self.decoder = Decoder(strict=False)

    def load(self, data: Any) -> Any:
        return self.decoder.decode(data)

    def dumps(self, data: Any, indent=4) -> str:
        return format(self.encoder.encode(data).decode(encoding="utf-8"), indent=indent)


JsonUtils = Json()


def read_json(path: str, **kwargs) -> Any:
    with open(path, **kwargs) as f:
        return JsonUtils.load(f.read())


def write_json(path: str, data: Any, **kwargs):
    with open(path, "w", **kwargs) as f:
        f.write(
            format(JsonUtils.encoder.encode(data).decode(encoding="utf-8"), indent=4)
        )
