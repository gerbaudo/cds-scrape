#!/bin/env python

# plot number of commens from CDS
#
# davide.gerbaudo@gmail.com
# Aug 2014

import ROOT as r
r.gROOT.SetBatch(1)

def main():
    input_filename='titles.txt' # from ./test_pymarc.py > titles.txt
    g_cit_vs_words = r.TGraph(0)
    g_cit_vs_words.SetName('g_cit_vs_words')
    g_cit_vs_words.SetTitle('N comments vs. N words in title; N words in title; N comments (including replies)')
    g_cit_vs_chars = r.TGraph(0)
    g_cit_vs_chars.SetName('g_cit_vs_chars')
    g_cit_vs_chars.SetTitle('N comments vs. N chars in title; N characters in title (incl. whitespace); N comments (including replies)')
    
    
    for l in open(input_filename).readlines():
        l.strip()
        tokens = l.split()
        if not len(tokens) : continue
        entry = tokens[0]
        num_cit = int(tokens[1])
        title = ' '.join(tokens[2:])
        print "{0}: {1} : {2}".format(entry, num_cit, title)
        g_cit_vs_words.SetPoint(g_cit_vs_words.GetN(), float(len(title.split())), float(num_cit)) 
        g_cit_vs_chars.SetPoint(g_cit_vs_chars.GetN(), float(len(title)), float(num_cit)) 
        

    c = r.TCanvas('c','')
    c.cd()
    for g, title in zip([g_cit_vs_words, g_cit_vs_chars],
                        ['Comments vs. words', 'Comments vs. chars']):
        c.Clear()
        g.SetMarkerStyle(r.kFullCircle)
        g.SetTitle(';'.join(["%s (corr. %.2f)"%(t, g.GetCorrelationFactor())
                             if 'vs' in t else t
                             for t in g.GetTitle().split(';')]))
        g.Draw('ap')
        c.Update()
        c.SaveAs(g.GetName()+'.png')
        
    out_file = r.TFile.Open('cds_stats.root', 'recreate')
    out_file.cd()
    g_cit_vs_words.Write()
    g_cit_vs_chars.Write()
    out_file.Write()
    out_file.Close()
if __name__=='__main__':
    main()

