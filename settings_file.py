#!/usr/bin/python -u
SETTINGS=\
{'host': {'TimeMode': {'default': 'NTP', 'name': 'time_mode', 'type': 's'},
          'TimeOwner': {'default': 'BMC', 'name': 'time_owner', 'type': 's'},
          'UseDhcpNtp': {'default': 'yes',
                         'name': 'use_dhcp_ntp',
                         'type': 's'},
          'bootflags': {'default': 'default',
                        'name': 'boot_flags',
                        'type': 's'},
          'bootpolicy': {'default': 'ONETIME',
                         'name': 'boot_policy',
                         'type': 's'},
          'networkconfig': {'default':
              'ipaddress=,prefix=,gateway=,mac=,addr_type=',
                            'name': 'network_config',
                            'type': 's'},
          'powercap': {'default': 0,
                       'max': 1000,
                       'min': 0,
                       'name': 'power_cap',
                       'type': 'i',
                       'unit': 'watts'},
          'powerpolicy': {'default': 'RESTORE_LAST_STATE',
                          'name': 'power_policy',
                          'type': 's'},
          'restrictedmode': {'default': False,
                             'name': 'restricted_mode',
                             'type': 'b'},
          'sysstate': {'default': '', 'name': 'system_state', 'type': 's'}}}
