# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2013 wangbuke <wangbuke@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': '读取客户上次订单价格',
    'version': '0.1',
    'category' : 'Sales Management',
    'description': """
功能：自动读取客户上次订单价格

具体流程：

在新建报价单读取产品价格时
1. 读取客户的价格表，如果有自定义的价格表，则按照原流程读取客户价格表。
2. 如果客户使用默认价格表，则搜索客户上一次订单（已确认和完成状态）的产品价格。
3. 返回新的价格

""",
    'author': 'wangbuke@gmail.com',
    'website': 'http://buke.github.io',
    'depends': ['sale'],
    'data': [
    ],
    'installable': True,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
