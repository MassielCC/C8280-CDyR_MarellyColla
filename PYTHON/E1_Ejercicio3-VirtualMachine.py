import time
import random

class VirtualMachine:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources
        self.running = False
        self.failed = False

    def start(self):
        if not self.failed:
            self.running = True
            print(f"VM {self.name} ha sido iniciada.")
        else:
            print(f"VM {self.name} no puede ser iniciada debido a un fallo.")

    def stop(self):
        self.running = False
        print(f"VM {self.name} ha sido detenida.")

    def restart(self):
        if not self.failed:
            self.stop()
            time.sleep(1)  # Simula el tiempo de reinicio
            self.start()
            print(f"VM {self.name} ha sido reiniciada.")
        else:
            print(f"VM {self.name} no puede ser reiniciada debido a un fallo.")
    
    def fail(self):
        self.failed = True
        self.running = False
        print(f"VM {self.name} ha fallado.")

    def recover(self):
        self.failed = False
        print(f"VM {self.name} ha sido recuperada.")

class Hypervisor:
    def __init__(self):
        self.vms = []

    def add_vm(self, vm):
        self.vms.append(vm)
        print(f"VM {vm.name} ha sido añadida al hipervisor.")

    def start_vm(self, name):
        vm = self.find_vm(name)
        if vm:
            vm.start()

    def stop_vm(self, name):
        vm = self.find_vm(name)
        if vm:
            vm.stop()

    def restart_vm(self, name):
        vm = self.find_vm(name)
        if vm:
            vm.restart()

    def fail_vm(self, name):
        vm = self.find_vm(name)
        if vm:
            vm.fail()

    def recover_vm(self, name):
        vm = self.find_vm(name)
        if vm:
            vm.recover()

    def allocate_resources(self):
        for vm in self.vms:
            if vm.running and not vm.failed:
                vm.resources = random.randint(1, 100)
                print(f"Recursos asignados a VM {vm.name}: {vm.resources}")

    def balance_load(self):
        total_resources = sum(vm.resources for vm in self.vms if vm.running and not vm.failed)
        if total_resources > 0:
            average_resources = total_resources // len([vm for vm in self.vms if vm.running and not vm.failed])
            for vm in self.vms:
                if vm.running and not vm.failed:
                    vm.resources = average_resources
                    print(f"Recursos balanceados para VM {vm.name}: {vm.resources}")

    def find_vm(self, name):
        for vm in self.vms:
            if vm.name == name:
                return vm
        print(f"VM {name} no encontrada.")
        return None
    
# Ejemplo de ejecución del simulador de hipervisor
if __name__ == "__main__":
    # Crear el hipervisor
    hypervisor = Hypervisor()

    # Crear y agregar VMs al hipervisor
    vm1 = VirtualMachine("VM1", 50)
    vm2 = VirtualMachine("VM2", 30)
    vm3 = VirtualMachine("VM3", 70)

    hypervisor.add_vm(vm1)
    hypervisor.add_vm(vm2)
    hypervisor.add_vm(vm3)

    # Iniciar VMs
    hypervisor.start_vm("VM1")
    hypervisor.start_vm("VM2")

    # Asignación de recursos
    hypervisor.allocate_resources()

    # Simulación de fallo y recuperación
    hypervisor.fail_vm("VM2")
    hypervisor.recover_vm("VM2")
    hypervisor.restart_vm("VM2")

    # Balanceo de carga
    hypervisor.balance_load()

    # Parar VMs
    hypervisor.stop_vm("VM1")
    hypervisor.stop_vm("VM2")
    hypervisor.stop_vm("VM3")