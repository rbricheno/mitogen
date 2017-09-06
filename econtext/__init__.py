"""
On the econtext master, this is imported from ``econtext/__init__.py`` as would
be expected. On the slave, it is built dynamically during startup.
"""

#: This is ``True`` in slave contexts. It is used in single-file Python
#: programs to avoid reexecuting the program's :py:func:`main` function in the
#: slave. For example:
#:
#:      .. code-block:: python
#:
#:          def do_work():
#:              os.system('hostname')
#:
#:          def main(broker):
#:              context = econtext.master.connect(broker)
#:              context.call(do_work)  # Causes slave to import __main__.
#:
#:          if __name__ == '__main__' and not econtext.slave:
#:              import econtext.utils
#:              econtext.utils.run_with_broker(main)
#:
slave = False


#: This is ``0`` in a master, otherwise it is a master-generated ID unique to
#: the slave context.
context_id = 0


#: This is ``None`` in a master, otherwise it is the master-generated ID unique
#: to the slave's parent context.
parent_id = None
