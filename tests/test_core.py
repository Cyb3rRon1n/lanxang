from lanxang.core.context import LanxangContext
from lanxang.core.registry import ModuleRegistry
from lanxang.core.runtime import LanxangRuntime
from lanxang.events import EventBus
from lanxang.intelligence.context import LanxangEnvironmentContext


def test_atlas_context_defaults_are_empty_dicts():

    context = LanxangContext()

    assert context.config == {}
    assert context.inventory == {}
    assert context.docker == {}
    assert context.proxmox == {}
    assert context.services == {}
    assert context.health == {}


def test_module_registry_register_get_all():

    registry = ModuleRegistry()
    registry.register("docker", "docker-module")

    assert registry.get("docker") == "docker-module"
    assert registry.get("missing") is None
    assert registry.all() == {"docker": "docker-module"}


def test_atlas_runtime_wires_context_environment_and_events(isolated_cwd):

    runtime = LanxangRuntime()

    assert runtime.get_context().config["name"] == "lanxang-node"
    assert isinstance(runtime.get_environment(), LanxangEnvironmentContext)
    assert isinstance(runtime.events, EventBus)
