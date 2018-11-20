from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb7-1kGYOGGvcOn99H7FEuQVZFQtQuZ_lCDkJ4IayVvqGndj6alyl7KXK4ZixSucwvy-iRwDHz56lj4_LxRUAwi4QUsrM9VTZ2m0jqsiJrzw-OKhOBebiBut5e6VRQLI-ClJxqbnEu83XZkh4xlrriyplWauEVZF1xn_M9NCKtxQ3kh-46rjaPavj8LknnIj38Bx_v'


def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
