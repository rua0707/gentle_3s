using System;
using System.Collections.Generic;
using System.Linq;

public class ReportData
{
    public HashSet<string> ReportPeople { get; set; }
    public string Name { get; set; }
    public int ReportCount { get { return ReportPeople.Count; } }
}
public class reportResult
{
    public int[] solution(string[] id_list, string[] report, int k)
    {
        if (k >= id_list.Length)
        {
            return new int[id_list.Length];
        }

        Dictionary<string, int> result = new Dictionary<string, int>();
        ReportData[] rDatas = new ReportData[id_list.Length];

        for (int i = 0; i < id_list.Length; i++)
        {
            result.Add(id_list[i], 0);
            rDatas[i] = new ReportData { Name = id_list[i], ReportPeople = new HashSet<string>() };
        }

        foreach (string ids in report)
        {
            string[] id = ids.Split(' ');
            rDatas.First(x => x.Name == id[1]).ReportPeople.Add(id[0]);
        }

        for (int i = 0; i < id_list.Length; i++)
        {
            if (rDatas[i].ReportCount < k)
            {
                continue;
            }

            foreach (var id in rDatas[i].ReportPeople)
            {
                result[id]++;
            }
        }

        return result.Select(x => x.Value).ToArray();
    }
}