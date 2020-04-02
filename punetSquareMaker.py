import argparse

parser = argparse.ArgumentParser(
    description="Takes the genotypes of parents and then determines the ratios of phenotypes" +
    "\n\nBoth parents genotypes are required",
    formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument(
    "-m", "--mother", action="store", dest="m_genes", required=True,
    help="Give the genotype of the mother")
parser.add_argument(
    "-f","--father", action="store", dest="f_genes", required=True,
    help="Give the genotype of the father")
args = parser.parse_args()



def main(): 
    if len(args.m_genes)!=len(args.f_genes):
        print("Please make sure genotypes of both parents are of same lenght")
        sys.exit()
    f_combs = gene_combos(args.f_genes)
    m_combs = gene_combos(args.m_genes)
    print("Father gene:", args.f_genes)
    print("Mother genes:", args.m_genes)
    print("length of gene: ", int(len(args.f_genes)/2))
    
    #print(f_combs)
    #print(m_combs)
    genotypes = genotypecombos(f_combs, m_combs)
    print_table(f_combs, m_combs, genotypes)
    calculate_prob(genotypes)

def genotypecombos(f_combs, m_combs): 
    print("father", f_combs)
    print("mother", m_combs)
    genotypes = []
    for f in f_combs: 
        for m in m_combs: 
            pair = f+m
            print("f",f,"m",m,pair)
            genotypes.append(pair)
    return genotypes

def print_table(f_combs, m_combs,genotypes):
     
    border = '-'*(7*len(f_combs)+1)
    string_of_genes = "    "
    print("here is your table father's genes are on top")
    for f in f_combs: 
        string_of_genes += "  "+f+"   "
    print(string_of_genes)
    print("  ",border)    
    s_of_genotypes = ""
    for j in range(len(f_combs)): 
        for i in range(len(f_combs)):
            s_of_genotypes += "" +  genotypes[j+i*4]+" | " 
        print(m_combs[j],'|',s_of_genotypes)
        print("  ",border)
        s_of_genotypes = ""

def calculate_prob(genotypes):
    gntypes = []
    probs = []
    for g in genotypes:
        i = 0
        if g not in gntypes: 
            gntypes.append(g)
            for j in genotypes: 
                if g == j: 
                    i+=1
            probs.append(float(i/16))
    print (gntypes)
    print (probs)

def gene_combos(genes):
    combos =[]
    for i in range(int(len(genes)/2)):
        if i == 0:
            combination = genes[i]+(genes[i+2])
            combos.append(combination)
            combination = genes[i]+(genes[i+3])
            combos.append(combination)
        else: 
            combination = genes[i]+(genes[i+1])
            combos.append(combination)
            combination = genes[i]+(genes[i+2])
            combos.append(combination)
    return combos
        
if __name__ == '__main__':
    main()
