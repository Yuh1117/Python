import json


def load_employees():
    with open("em.json", encoding="utf-8") as f:
        return json.load(f)


def display(data):
    for em in data:
        for k, v in em.items():
            if k.__eq__("ma_nv"):
                print(f"Ma nhan vien: {v}")
            elif k.__eq__("ten_nv"):
                print(f"Ten nhan vien: {v}")


def add_em(data, ma, ten):
    em = {
        "ma_nv": ma,
        "ten_nv": ten
    }
    data.append(em)
    with open("em.json", mode="w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def search_em(data, ten):
    # kq = []
    # for em in data:
    #     if em["ten_nv"].find(ten) >= 0:
    #        kq.append(em)
    # return kq
    return [em for em in data if em["ten_nv"].find(ten) >= 0]


def delete_em(data, ma):
    for idx, em in enumerate(data):
        if em["ma_nv"] == ma:
            del data[idx]
    with open("em.json", mode="w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

if __name__ == '__main__':
    data = load_employees()
    display(data)
    # add_em(data, "98", "vpgh")
    # display(data)
    print("-------------")
    kq = search_em(data, "Thanh")
    display(kq)
    print("-------------")
    delete_em(data, '98')
