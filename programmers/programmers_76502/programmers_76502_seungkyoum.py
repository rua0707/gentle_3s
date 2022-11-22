def solution(s):
    s_list = list(s)
    answer = 0

    for _ in range(len(s)):
        st = []

        for i in s_list:
            if len(st) > 0:
                if st[-1] == "(" and i == ")":
                    st.pop()
                elif st[-1] == "[" and i == "]":
                    st.pop()
                elif st[-1] == "{" and i == "}":
                    st.pop()
                else:
                    st.append(i)
            else:
                st.append(i)
        
        if len(st) == 0:
            answer += 1
        s_list.append(s_list.pop(0))

    return answer