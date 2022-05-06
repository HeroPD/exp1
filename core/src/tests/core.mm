#include <pybind11/pybind11.h>
// #include "export.h"
#include <Cocoa/Cocoa.h>

namespace py = pybind11;


@interface AppDelegate : NSObject<NSApplicationDelegate, NSWindowDelegate>

@end

@implementation AppDelegate : NSObject

- (id)init {
    self = [super init];
    return self;
}

- (void)applicationDidFinishLaunching:(NSNotification *)notification {
    
}

- (BOOL) applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)application
{
    return YES;
}

@end

@interface MainView : NSView

@end

int add(int i, int j) {
    return i + j;
}

int main() {
    printf("change");
    return 12;
}


PYBIND11_MODULE(core, m) {
    m.def("add", &add, "A function that adds two numbers");
    m.def("main", &main, "Main funtion");
}
