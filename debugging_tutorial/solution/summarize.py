
import pandas as pd
import pylab as plt


def get_means():
	homosap = pd.read_csv('output/human_proteome.csv', index_col=0)
	chimp = pd.read_csv('output/chimp_proteome.csv', index_col=0)
	banana = pd.read_csv('output/banana_proteome.csv', index_col=0)

	means = pd.DataFrame(data = {
		'human': homosap[homosap.columns[2:]].mean(),
		'chimp': chimp[chimp.columns[2:]].mean(),
		'banana': banana[banana.columns[2:]].mean(),
		})
	return means


def calc_z(means):
	z = pd.DataFrame({
	        'chimp': means['human'] / means['chimp'] - 1.0,
	        'banana': means['human'] / means['banana'] - 1.0
	        })
	z.plot.bar()
	plt.title('Proteome diversity')
	plt.ylabel('ratio of means human/x - 1.0')
	plt.xlabel('amino acid')
	plt.savefig('barplot.png')
	return z


	
if __name__ == '__main__':
    means = get_means()
    print(means.sum())

    z = calc_z(means)
    print(z.abs().mean())
