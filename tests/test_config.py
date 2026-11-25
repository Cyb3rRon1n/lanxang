from lanxang.config.loader import load_config
from lanxang.config.models import LanxangConfig


def test_load_config_defaults_when_no_file(isolated_cwd):

    config = load_config()

    assert config == LanxangConfig()
    assert config.name == "lanxang-node"
    assert config.intelligence.provider == "none"
    assert config.intelligence.model == ""                  # no AI: no model


def test_load_config_reads_atlas_yaml(isolated_cwd):

    (isolated_cwd / "lanxang.yaml").write_text(
        "name: homelab\n"
        "discovery:\n"
        "  hardware: false\n"
        "intelligence:\n"
        "  provider: ollama\n"
        "  model: llama3.1\n"
    )

    config = load_config()

    assert config.name == "homelab"
    assert config.discovery.hardware is False
    assert config.discovery.storage is True
    assert config.intelligence.provider == "ollama"
    assert config.intelligence.model == "llama3.1"


def test_model_defaults_follow_the_provider():
    from lanxang.config.models import IntelligenceConfig

    assert IntelligenceConfig(provider="ollama").model == "qwen3:8b"
    assert IntelligenceConfig(provider="anthropic").model == "claude-opus-5"
    assert IntelligenceConfig(provider="ollama", model="llama3.1").model == "llama3.1"
