def calc(pheptinh):  
    def exp(x):
        if x>=0:
            # Su dung chuoi Taylor de tinh e^x
            n_terms = 20  # So hang trong chuoi Taylor
            par_int = 1
            par_frac = 1
            e= 2.718281828459045
            x_int = int(x)
            x_frac = x - x_int
            for n in range(x_int):
                par_int *= e  # e^x_int  = e * e * ... (x_int lan)
        
            factorial = 1
            for n in range(1, n_terms + 1):
                factorial *= n  # tinh n!
                term = (x_frac ** n) / factorial  # tinh so hang thu n cua chuoi Taylor
                par_frac += term
        
            result = par_int * par_frac
            return result
        else:
            return 1 / exp(-x)

    def sinh(x):
        return (exp(x) - exp(-x)) / 2

    def cosh(x):
        return (exp(x) + exp(-x)) / 2

    def tanh(x):
        return sinh(x) / cosh(x)

    def ln(x, so_hang=100):
        # Hàm tính ln(x) bằng chuỗi Taylor, có điều chỉnh cho x lớn/nhỏ
        if x <= 0:
            raise ValueError("ln(x) không xác định với x ≤ 0")
        # Diều chỉnh x về khoảng [0,1] bằng cách chia cho e^k
        k = 0
        while exp(k) < x:
            k += 1
        x/=exp(k)
        # Tính phần ln(x) khi đã điều chỉnh
        y = (x - 1) / (x + 1)
        y_mu = y
        ket_qua = 0.0

        for i in range(1, so_hang * 2, 2):  # i = 1, 3, 5, ...
            ket_qua += y_mu / i
            y_mu *= y * y

        # Cộng thêm phần bù ln(2)*k (vì mỗi lần chia/nhân 2)
        return 2 * ket_qua + k  # ln(2) ≈ 0.6931

    pi=3.141592653589793

    def arcsin(x):
        # Kiểm tra miền xác định
        if x < -1 or x > 1:
            raise ValueError("arcsin(x) chỉ xác định khi -1 ≤ x ≤ 1")

        # Nếu |x| nhỏ → dùng khai triển Taylor quanh 0
        elif x<=sqrt(2)/2 and x>=-sqrt(2)/2:
            ket_qua = 0.0
            tu = 1.0
            mau = 1.0
            x_mu = x
            for n in range(50):  # 50 số hạng là đủ
                if n > 0:
                    tu *= 2*n - 1
                    mau *= 2*n
                he_so = tu / (mau * (2*n + 1))
                ket_qua += he_so * x_mu
                x_mu *= x*x
            return ket_qua
        elif x > 0:
            return arccos(sqrt(1 - x*x))
        else:
            return -arccos(sqrt(1 - x*x))

    def arccos(x):
        # Kiểm tra miền xác định
        if x < -1 or x > 1:
            raise ValueError("arcsin(x) chỉ xác định khi -1 ≤ x ≤ 1")

        # Nếu |x| nhỏ → dùng khai triển Taylor quanh 0
        elif x<=sqrt(2)/2 and x>=-sqrt(2)/2:
            ket_qua = pi/2
            tu = 1.0
            mau = 1.0
            x_mu = x
            for n in range(50):  # 50 số hạng là đủ
                if n > 0:
                    tu *= 2*n - 1
                    mau *= 2*n
                he_so = tu / (mau * (2*n + 1))
                ket_qua -= he_so * x_mu
                x_mu *= x*x
            return ket_qua
        elif x > 0:
            return arcsin(sqrt(1 - x*x))
        else:
            return pi - arcsin(sqrt(1 - x*x))

    def arctan(x):
        return arcsin(x / ((x*x + 1)**0.5))

    def sin(x, n=20):
        # Đưa góc về [-pi, pi] để chuỗi hội tụ nhanh hơn vì sin(x) lặp lại theo chu kỳ 2pi
        x = ((x + pi) % (2 * pi)) - pi

        sin_x = 0
        sign = 1  # dấu xen kẽ +, -
        factorial = 1

        # Tính n hạng đầu tiên
        for k in range(n):
            if k > 0:
                factorial *= 2*k * ( 2*k + 1 )
            else:
                factorial = 1
            term = sign * (x ** (2 * k + 1)) / factorial #Công thức Taylor của sin(x)
            sin_x += term
            sign *= -1 #Đảo dấu sau mỗi vòng lặp
        return sin_x


    def cos(x, n=20):
        # Rút gọn góc về [-pi, pi]
        x = ((x + pi) % (2 * pi)) - pi

        cos_x = 0
        sign = 1
        factorial = 1

        for k in range(n):
            if k > 0:
                factorial *= (2*k - 1) * (2*k)
            else:
                factorial = 1

            term = sign * (x ** (2 * k)) / factorial #Công thức Taylor của cos(x)
            cos_x += term
            sign *= -1
        return cos_x

    #tan(x) = sin(x)/cos(x)
    def tan(x, n=20):
        c = cos(x, n)
        #Kiểm tra miền xác định (kiểm tra xem cos(x) có quá gần 0)
        if c < 1e-15 and c > -1e-15:
            raise ValueError("tan(x) không xác định (cos(x) = 0)")
        return sin(x, n) / c


    def sqrt(x, n=20):
        # Hàm tính căn bậc hai của x bằng khai triển Taylor quanh 1
        # Có chia / nhân 4 để đảm bảo hội tụ tốt
        if x < 0:
            raise ValueError("Không thể lấy căn của số âm")
        if x == 0:
            return 0.0

        # Đưa x về y sao cho y nằm trong (0, 2)
        m = 0
        y = x
        while y >= 2:
            y /= 4
            m += 1
        while y < 0.5:
            y *= 4
            m -= 1

        # Tính sqrt(y) bằng khai triển Taylor của sqrt(1 + t), t = y - 1
        t = y - 1
        c = 1.0          # hệ số đầu tiên C(1/2, 0)
        t_pow = 1.0      # t^0
        result = 1.0     # tổng ban đầu

        for k in range(1, n):
            c *= (0.5 - (k - 1)) / k      # hệ số nhị thức C(1/2, k)
            t_pow *= t                    # t^k
            result += c * t_pow           # cộng thêm từng hạng

        #sqrt(x) = 2^m * sqrt(y)
        return (2 ** m) * result

    ketqua=eval(pheptinh)
    return ketqua
