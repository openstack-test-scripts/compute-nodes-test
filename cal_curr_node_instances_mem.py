from oslo_log import log as logging

import nova.conf
from nova import config
from nova import objects
from nova import context

LOG = logging.getLogger(__name__)
CONF = nova.conf.CONF

if __name__ == "__main__":
    default_config_files = ['/etc/nova/nova.conf']
    host_name = 'dfcompute3'
    argv = []
    context = context.get_admin_context()
    expected_attrs = ['system_metadata', 'numa_topology',
                      'flavor', 'migration_context']
    memory_mb_used = 512

    config.parse_args(argv, default_config_files=default_config_files)
    objects.register_all()

    instances = objects.InstanceList.get_by_host(context, host_name,
                                                 expected_attrs=expected_attrs)

    for instance in instances:
        memory_mb_used += 1 * instance['memory_mb']
        print instance.vm_state, instance.task_state
    print memory_mb_used
