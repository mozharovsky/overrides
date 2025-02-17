#
#  Copyright 2016-2021 Keunhong Lee & Eugene Mozharovsky
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from typing import Callable, TypeVar


FuncType = TypeVar("FuncType", bound=Callable)


def final(func: FuncType) -> FuncType:
    """Decorator to indicate that the decorated method is finalized and cannot be overridden.
    The decorator code is executed while loading class. Using this method
    should have minimal runtime performance implications.
    Currently, only methods with `@override` are checked.

    How to use:
    ```
    from overrides import final

    class SuperClass(object):
        @final
        def method(self):
          return 2

    class SubClass(SuperClass):
        @overrides
        def method(self): #causes an error
            return 1
    ```

    :raises  `AssertionError` if there exists a match in sub classes for the method name
    :return  original method
    """
    setattr(func, "__finalized__", True)
    return func
