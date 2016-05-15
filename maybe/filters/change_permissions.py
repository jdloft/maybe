# maybe - see what a program does before deciding whether you really want it to happen
#
# Copyright (c) 2016 Philipp Emanuel Weidmann <pew@worldwidemann.com>
#
# Nemo vir est qui mundum non reddat meliorem.
#
# Released under the terms of the GNU General Public License, version 3
# (https://gnu.org/licenses/gpl.html)


from maybe import T, register_filter, descriptor_path, full_path


def format_permissions(permissions):
    result = ""
    for i in range(2, -1, -1):
        result += "r" if permissions & (4 * 8**i) else "-"
        result += "w" if permissions & (2 * 8**i) else "-"
        result += "x" if permissions & (1 * 8**i) else "-"
    return result


def filter_change_permissions(path, permissions):
    return "%s of %s to %s" % (T.yellow("change permissions"), T.underline(path),
                               T.bold(format_permissions(permissions))), 0


filter_scope = "change_permissions"

register_filter(filter_scope, "chmod", lambda pid, args:
                filter_change_permissions(full_path(pid, args[0]), args[1]))
register_filter(filter_scope, "fchmod", lambda pid, args:
                filter_change_permissions(descriptor_path(pid, args[0]), args[1]))
register_filter(filter_scope, "fchmodat", lambda pid, args:
                filter_change_permissions(full_path(pid, args[1], args[0]), args[2]))
